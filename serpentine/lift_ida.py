from ida_bytes import get_bytes, next_head
from ida_ua import insn_t, decode_insn
from idautils import XrefsTo, Segments
from ida_segment import get_segm_name, get_segm_by_name, getseg
from idc import print_insn_mnem, get_operand_value, get_wide_byte, print_operand, get_item_end, get_operand_type, o_mem
import ida_segment

def is_mov_instruction(ea):
    """Check if the instruction at ea is a MOV instruction."""
    mnem = print_insn_mnem(ea)
    return mnem == "mov"

def find_patterns():
    """
    Find instances of the pattern:
        pop     cs:qword_X
        push    rax
        mov     rax, 0
        mov     ah, byte ptr cs:loc_Y
        lea     eax, [eax+constant]
        mov     cs:dword_Z, eax
        pop     rax
    """
    patterns = []

    # Iterate through segments
    for seg_ea in Segments():
        seg = getseg(seg_ea)
        if seg:
            # Get segment name
            name = ida_segment.get_segm_name(seg)
            if name == ".data":
                current_ea = seg_ea
                while current_ea < seg.end_ea:
                    if match_pattern(current_ea, seg.end_ea):
                        patterns.append(current_ea)
                    current_ea = next_head(current_ea, seg.end_ea)

    return patterns

def match_pattern(ea, end_ea):
    """Check if the sequence starting at ea matches our pattern."""
    # First instruction should be pop cs:qword
    if print_insn_mnem(ea) != "pop":
        return False

    # Second instruction should be push rax
    next_ea = next_head(ea, end_ea)
    if print_insn_mnem(next_ea) != "push" or "rax" not in print_operand(next_ea, 0):
        return False

    # Third instruction should be mov rax, 0
    next_ea = next_head(next_ea, end_ea)
    if not is_mov_instruction(next_ea) or get_operand_value(next_ea, 1) != 0:
        return False

    # Fourth instruction should be mov ah, byte ptr cs:loc
    next_ea = next_head(next_ea, end_ea)
    if not is_mov_instruction(next_ea) or "ah" not in print_operand(next_ea, 0):
        return False

    # Fifth instruction should be lea eax
    next_ea = next_head(next_ea, end_ea)
    if print_insn_mnem(next_ea) != "lea" or "eax" not in print_operand(next_ea, 0):
        return False

    # Sixth instruction should be mov cs:dword
    next_ea = next_head(next_ea, end_ea)
    if not is_mov_instruction(next_ea):
        return False

    # Last instruction should be pop rax
    next_ea = next_head(next_ea, end_ea)
    if print_insn_mnem(next_ea) != "pop" or "rax" not in print_operand(next_ea, 0):
        return False

    return True

def sign_extend(value, bits):
    """Sign extend a value based on its bit width."""
    sign_bit = 1 << (bits - 1)
    extended = (value & (sign_bit - 1)) - (value & sign_bit)
    if bits == 64:  # Ensure we keep full 64 bits for addresses
        return extended & 0xFFFFFFFFFFFFFFFF
    return extended

def get_signed_operand_value(ea, n):
    """Get operand value and sign extend it if it's negative."""
    value = get_operand_value(ea, n)
    # For addresses, use 64 bits
    if value > 0xFFFFFFFF:
        return value  # Keep as is if it's a 64-bit address
    # For immediates, use 32 bits
    return sign_extend(value, 32)

def patch_block(pattern_ea):
    """Calculate the value of eax at the lea instruction."""
    # Get segment end for next_head
    seg = getseg(pattern_ea)
    end_ea = seg.end_ea

    # Navigate to mov ah instruction
    current_ea = pattern_ea
    for _ in range(2):  # Skip pop, push, mov rax
        current_ea = next_head(current_ea, end_ea)
    mov_ah_ea = next_head(current_ea, end_ea)  # Get to mov ah

    # Get the memory operand of mov ah instruction
    address = get_signed_operand_value(mov_ah_ea, 1)

    # Take the "ah" portion of the address
    ah = get_wide_byte(address) << 8

    # Navigate to lea instruction
    lea = next_head(mov_ah_ea, end_ea)

    # Get the memory operand of lea instruction
    offset = get_signed_operand_value(lea, 1)

    final_eax = ah + offset
    print()
    return final_eax

def main():
    print("Searching for patterns...")
    patterns = find_patterns()

    if not patterns:
        print("No matching patterns found.")
        return

    print(f"Found {len(patterns)} matching patterns.")

    for pattern_ea in reversed(patterns):
        print(f"\nPattern at 0x{pattern_ea:X}")
        final_value = patch_block(pattern_ea)

if __name__ == "__main__":
    main()
