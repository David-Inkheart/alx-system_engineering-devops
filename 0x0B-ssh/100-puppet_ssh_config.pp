# Using Puppet, create a configuration file
include stdlib
# Declare the ssh_config file as a File resource
file { '/etc/ssh/ssh_config':
  ensure  => file,
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
}

# Declare the identity file
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
}
