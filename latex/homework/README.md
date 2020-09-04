### Setup

See https://medium.com/@rcpassos/writing-latex-documents-in-visual-studio-code-with-latex-workshop-d9af6a6b2815

#### Mac

- Install MacTex without GUI

```
# macOS MacTex Install
brew cask install mactex-no-gui

# Updating the packages
sudo tlmgr update --self && sudo tlmgr update --all
```

- Install Perl modules required for the formatter `latexindex`

```
cpan install Log::Log4perl
cpan install Log::Dispatch::File
cpan install YAML::Tiny
cpan install File::HomeDir
```

- Install LaTeX Workshop plugin for Visual Studio Code
  - Set setting `latex-workshop.latex.outDir` to `%DIR%/dist/`

### Workflow

- Update `.tex` files on Visual Studio Code.
- Output file `dist/main.pdf` will be automatically generated.

