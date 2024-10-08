import hashlib
import itertools

def md5_bruteforce(known, target_md5):
    underscore_positions = [i for i, c in enumerate(known) if c == '_']
    num_underscores = len(underscore_positions)
    for candidate in itertools.product(range(256), repeat=num_underscores):
        filled_known = list(known)
        for i, pos in enumerate(underscore_positions):
            filled_known[pos] = chr(candidate[i])
        candidate_string = ''.join(filled_known)
        candidate_md5 = hashlib.md5(candidate_string.encode()).hexdigest()
        if candidate_md5 == target_md5:
            return candidate_string
    return None

# known = 'ru_e fl_reon { s_ring_: $f__ "1RuleA_ayK33p$M_lw4r3Aw4y@fl_re-on._om" cond__ion: $f _'
known = 'rule flareon { strings: $f = "1RuleA_ayK33p$M_lw4r3Aw4y@flare-on.com" condition: $f }'
target_md5 = 'b7dc94ca98aa58dabb5404541c812db2'

result = md5_bruteforce(known, target_md5)

if result:
    print(f"Found matching string: {result}")
else:
    print("No matching string found.")
