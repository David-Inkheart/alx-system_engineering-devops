# Using Puppet, create a configuration file
$var = "Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no"

file { '/root/.ssh/config':
    ensure  => file,
    content => $var,
}
