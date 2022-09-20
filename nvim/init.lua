-------------------------------
--Plugins and Language Servers
-------------------------------
require('plugins')
require'lspconfig'.pyright.setup{}
--require'lspconfig'.tsserver.setup{}
--require'lspconfig'.rust_analyzer.setup{}

--------------
--Basic Setup
--------------
local cmd = vim.cmd    -- to execute Vim commands e.g. cmd('pwd')
local fn = vim.fn      -- to call Vim functions e.g. fn.bufnr()
local g = vim.g        -- a table to access global variables
local opt = vim.opt    -- to set options
local key = vim.keymap -- to set key mappings
opt.encoding='utf-8'
opt.backspace='indent,eol,start'
cmd 'filetype plugin indent on'
opt.tabstop=4
opt.softtabstop=4
opt.shiftwidth=4
opt.hidden=true
opt.hlsearch=true
opt.incsearch=true
opt.ignorecase=true
opt.smartcase=true
opt.wildmenu=true
opt.mouse='a'

------------------
--Visual Settings
------------------
cmd 'syntax on'
opt.ruler=true
opt.number=true
opt.colorcolumn='80'
cmd 'let no_buffers_menu=1'
cmd 'colorscheme onedark'
--g['lightline#colorscheme']='one_dark' --?

--nerdtree settings for netrw
g['netrw_banner'] = 0
g['netrw_liststyle'] = 3
g['netrw_browse_split'] = 3
g['netrw_altv'] = 1
g['netrw_winsize'] = 20

-----------
--Mappings
-----------
key.set('n', '<c-E>', ':Vexplore<CR>')
key.set('n', '<f5>', ':sp<CR> :term python %<CR>')
key.set('n', '<c-W>', ':bd!<CR>') --destroy window
--key.set('n', '<c-O>', '<c-C><c-O>')
--key.set('n', '<space>'

--------
--Other
--------
--vim script
cmd([[
let g:lightline = {
      \ 'colorscheme': 'one',
      \ }

autocmd BufWritePost *.py call flake8#Flake8()

augroup ProjectDrawer
  autocmd!
  autocmd VimEnter * if argc() == 0 | Vexplore | endif
augroup END

]])
