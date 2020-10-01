# Fixes the holberton container using apuppet script
$fix = "/usr/bin/env sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"

exec { 'fix line 137':
  command => $fix
}

service { 'apache2':
  ensure  => 'running'
}
