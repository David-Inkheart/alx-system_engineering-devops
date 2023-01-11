# Using Puppet, create a configuration file
$var = 'Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no'

file { '/root/.ssh/config':
    content => '$var',
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
}
