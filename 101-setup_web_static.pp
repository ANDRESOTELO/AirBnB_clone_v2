# Puppet for setup

exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
file { '/data':
  ensure => directory
}
->
file { '/data/web_static':
  ensure => directory
}
->
file { '/data/web_static/shared':
  ensure => directory
}
->
file { '/data/web_static/releases':
  ensure => directory
}
->
file { '/data/web_static/releases/test':
  ensure => directory
}
->
file { '/data/web_static/releases/test/index.html':
  ensure => present
}
->
file_line { 'index':
  ensure => present,
  path   => '/data/web_static/releases/test/index.html',
  line   => 'Holberton School, Holberton is cool!',
}
->
exec { 'create symbolik link':
  command  => 'ln -s -f /data/web_static/releases/test/ /data/web_static/current',
  user     => 'root',
  provider => 'shell'
}
->
exec { 'Permissions':
  command  => 'chown -R ubuntu:ubuntu /data/',
  user     => 'root',
  provider => 'shell'
}
->
exec { 'Update the Nginx configuration':
  command  => 'sed -i "48i location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}
->
exec { 'restart nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
