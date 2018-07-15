set nocompatible              " be iMproved, required
filetype off                  " required set rtp+=~/.vim/bundle/Vundle.vim

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'L9'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'https://github.com/vim-scripts/tomatosoup.vim'
Plugin 'https://github.com/flazz/vim-colorschemes'
Plugin 'morhetz/gruvbox'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-airline/vim-airline' 
Plugin 'vim-scripts/Conque-Shell'
Plugin 'tpope/vim-surround'
Plugin 'python-mode/python-mode'
"Plugin 'davidhalter/jedi-vim'
Plugin 'lepture/vim-jinja'
Plugin 'sjl/gundo.vim'
Plugin 'rking/ag.vim'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"--------------------------------------------------------------------------------------------

let mapleader=","

set ls=2
set t_Co=256
highlight Nontext ctermbg=none
colorscheme gruvbox   
syntax enable

set ai
set smarttab
set tabstop=4
set softtabstop=4

set number
set showcmd

set cursorline
filetype indent on   
set wildmenu
set lazyredraw    

set incsearch
set hlsearch
nnoremap <leader><space> :nohlsearch<CR>

set foldenable
set foldlevelstart=10
set foldnestmax=10

nnoremap <space> za

set foldmethod=indent

nnoremap j gj
nnoremap k gk

nnoremap B ^
nnoremap E $
nnoremap $ <nop>
nnoremap ^ <nop>
nnoremap gV `[v`]

let mapleader=","  

inoremap jk <esc>

" Remove autohook of mouse of vim
if !has('gui_running')
set mouse= 
endif

" Move between windows
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

nnoremap <leader>t :NERDTree<CR>


"------------------------------------------------------------------------------------------
let g:jedi#popup_select_first = 0

" toggle gundo
nnoremap <leader>u :GundoToggle<CR>

nnoremap <F5> :ConqueTermSplit ipython<CR>

" save session
nnoremap <leader>s :mksession<CR>

nnoremap <leader>a :Ag<CR>
set listchars=tab:··
set list
