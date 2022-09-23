let
  pkgs = import <nixpkgs> { };

  pythonEnv = pkgs.python3.withPackages(ps: [
    ps.black
    ps.flake8
    ps.mypy
  ]);

in pkgs.mkShell {
  packages = [ pythonEnv ];
}
