{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: https://sourceforge.net/projects/libpng/files/libpng16/
		{ "url" : "https://sourceforge.net/projects/libpng/files/libpng16/1.6.36/libpng-1.6.36.tar.xz",	"hashes" : [ { "type" : "sha256", "sum" : "53e54609120f0cd5fb58eab4f0f40386d2f45a8469f5cd252da1b3b0" },	], },
		{ "url" : "https://fossies.org/linux/misc/libpng-1.6.36.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "53e54609120f0cd5fb58eab4f0f40386d2f45a8469f5cd252da1b3b0" }, ],	},
	],
	# 'custom_cflag' : '-fno-asynchronous-unwind-tables',
	'conf_system' : 'cmake',
	'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_BINARY=OFF -DCMAKE_BUILD_TYPE=Release -DPNG_TESTS=OFF -DPNG_SHARED=OFF -DPNG_STATIC=ON',
	# 'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --oldincludedir={target_prefix}/include',
	'patches' : [
		('https://raw.githubusercontent.com/DeadSix27/python_cross_compile_script/master/patches/libpng/libpng-1.6.36-apng.patch', '-p1'),
	],
	'depends_on' : [ 'zlib', ],
	'_info' : { 'version' : '1.6.36', 'fancy_name' : 'libpng' },
}