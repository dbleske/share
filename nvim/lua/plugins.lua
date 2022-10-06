return require('packer').startup(function(use) 

 -- Packer can manage itself
  use 'wbthomason/packer.nvim'
  use 'neovim/nvim-lspconfig'
  use 'itchyny/lightline.vim'
  use 'nvim-treesitter/nvim-treesitter'
  use 'nvie/vim-flake8'
  use 'hrsh7th/cmp-nvim-lsp'
  use 'hrsh7th/nvim-cmp'
  -- You can alias plugin names
  use {'joshdick/onedark.vim', as = 'onedark'}

end)
