# asd ajsdkaj skdnjas
exec {'remove lims':
  command => 'sed -rie \'s/(holberton (hard|soft) nofile).*/\1 1000/gi\' /etc/security/limits.conf',
  path    => 'usr/bin/:/bin/'
}
