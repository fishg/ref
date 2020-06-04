{
  'targets': [
    {
      'target_name': 'binding',
      'product_dir': '<(module_path)',
      'sources': [ 'src/binding.cc' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET":"10.9"
      }
    }
  ]
}
