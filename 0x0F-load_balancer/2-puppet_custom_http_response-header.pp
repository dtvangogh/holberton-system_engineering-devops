# ccustom header using puppet
$update = '/usr/bin/env apt-get -y update'
$command = "/usr/bin/env sed -i '14a add_header X-Served-By ${hostname};' /etc/nginx/nginx.conf"

exec { 'apt-get update':
  command => $update
}

-> package { 'nginx':
  ensure   => 'installed'
}

-> exec { 'custom HTTP header':
  command => $command
}

-> service { 'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart'
}
