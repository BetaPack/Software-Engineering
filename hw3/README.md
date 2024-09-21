# Vim/Neovim Plugin Setup

This repository demonstrates the setup of Vim (or Neovim) along with three essential plugins: **NERDTree**, **FuzzyFinder (fzf)**, and **CVcolorscheme**. These plugins enhance file navigation, fuzzy searching, and aesthetic appeal within the text editor.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation Steps](#installation-steps)
- [Plugin Installation](#plugin-installation)
- [Usage](#usage)
- [Key Bindings](#key-bindings)
- [Screenshots](#screenshots)
- [Submitting Homework](#submitting-homework)

---

## Introduction

Vim and Neovim are powerful text editors known for their efficiency, especially when combined with the right plugins. This guide will help you configure your Vim/Neovim setup with:
- **NERDTree**: A file system explorer.
- **FuzzyFinder (fzf)**: A fast fuzzy file finder.
- **CVcolorscheme**: A plugin that enhances the look and feel of Vim with custom color schemes.

By the end of this setup, you will have these plugins operational in Vim/Neovim, complete with customized key bindings.

---

## Requirements

- Vim or Neovim installed on your machine:
  - [Install Vim](https://www.vim.org/download.php)
  - [Install Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim)

- `vim-plug` plugin manager to install and manage plugins.

---

## Installation Steps

### 1. Install Vim or Neovim
- For Vim:
  ```bash
  sudo apt install vim
  ```
- FInstall vim-plug Plugin Manager
  Run the following command in your terminal to install vim-plug:
  ```bash
  curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  ```
- Configure .vimrc or init.vim
  Add the following plugin configuration in your .vimrc (for Vim) or init.vim (for Neovim) file:
  ```bash
  " Initialize the plugin manager (vim-plug)
  call plug#begin('~/.vim/plugged')
  
  " NERDTree for file navigation
  Plug 'preservim/nerdtree'
  
  " FuzzyFinder (fzf) for fast file searching
  Plug 'junegunn/fzf'
  Plug 'junegunn/fzf.vim'
  
  " CVcolorscheme for custom color schemes
  Plug 'ciaranm/cvcolorscheme'
  
  call plug#end()
  
  " Set options
  set number              " Show line numbers
  set tabstop=4           " Set tab width to 4 spaces
  set shiftwidth=4        " Use 4 spaces for indentation
  set expandtab           " Use spaces instead of tabs
  set autoindent          " Auto-indent new lines
  
  " Key bindings
  nnoremap <C-n> :NERDTreeToggle<CR>   " Toggle NERDTree with Ctrl + N
  nnoremap <C-p> :FZF<CR>              " Open FZF with Ctrl + P
  
  " Set colorscheme
  colorscheme cv
  ```
- Verifying Plugin Installation
  To verify that the plugins are installed and working:
  
  NERDTree: Use Ctrl + n to toggle the file explorer.
  FuzzyFinder: Use Ctrl + p to open the fuzzy file search.
  CVcolorscheme: The custom color scheme should be applied automatically when you open Vim.
