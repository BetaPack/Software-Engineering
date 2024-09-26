" Initialize the plugin manager (vim-plug)
call plug#begin('~/.vim/plugged')
  
" Add this line for the gruvbox plugin
Plug 'morhetz/gruvbox'

" NerdTree for file navigation
Plug 'preservim/nerdtree'

" FuzzyFinder for quick file search
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'

call plug#end()

" Set options
set number              " Show line numbers
set tabstop=4           " Set tab width to 4 spaces
set shiftwidth=4        " Use 4 spaces for indentation
set expandtab           " Use spaces instead of tabs
set autoindent          " Auto-indent new lines

" Key bindings
nnoremap <C-n> :NERDTreeToggle<CR>   " Toggle NerdTree with Ctrl + N

" FZF key binding
nnoremap <C-p> :FZF<CR>

colorscheme gruvbox
set background=light
