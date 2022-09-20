return require('packer').startup(function(use) 

 -- Packer can manage itself
  use 'wbthomason/packer.nvim'
  use 'neovim/nvim-lspconfig'
  use 'itchyny/lightline.vim'
  use 'nvim-treesitter/nvim-treesitter'
  use 'nvie/vim-flake8'
  -- You can alias plugin names
  use {'joshdick/onedark.vim', as = 'onedark'}

end)
