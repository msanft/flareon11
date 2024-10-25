{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/5b80e8c3bae3a182439a478713021109826dcb2d";
  };

  outputs =
    { self, nixpkgs }:
    let
      pkgs = import nixpkgs { system = "x86_64-linux"; };
    in
    {
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = [
          (pkgs.python3.withPackages (p: [ p.qiling p.miasm ]))
        ];
      };
    };
}
