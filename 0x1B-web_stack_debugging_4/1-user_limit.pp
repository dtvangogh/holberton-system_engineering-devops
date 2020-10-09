# fixes the server
$script = "/usr/bin/env sed -i 's/nofile [0-9]/nofile 10240/g' /etc/security/limits.conf"

exec { 'Change OS config to allow login with Holberton user':
  command => $script
}
