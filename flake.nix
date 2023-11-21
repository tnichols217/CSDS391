{
  description = "Dev shell";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    gitignore = {
      url = "github:hercules-ci/gitignore.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    dream2nix.url = "github:nix-community/dream2nix";
  };

  outputs = { self, nixpkgs, flake-utils, dream2nix, gitignore }:
    let
      customOut = flake-utils.lib.eachDefaultSystem (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in with pkgs; 
        {
          devShells = rec {
            main = pkgs.mkShell {
              packages = [
                (python3.withPackages (ps: with ps; [
                    pandas
                    requests
                    pip
                    jupyter
                    black
                    numpy
                    matplotlib
                    scipy
                    pygobject3
                  ])
                )
                nodePackages.nodemon
              ];
            };

            default = main;

          };
        });
    in
    customOut;
}