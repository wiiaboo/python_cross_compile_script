{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/shaderc.git',
	'configure_options' :
		'cmake .. {cmake_prefix_options} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DCMAKE_TOOLCHAIN_FILE=cmake/linux-mingw-toolchain.cmake '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSHADERC_SKIP_INSTALL=ON '
		'-DSHADERC_SKIP_TESTS=ON '
		'-DSHADERC_ENABLE_SPVC=ON '
		'-DMINGW_COMPILER_PREFIX={cross_prefix_bare} '
	, #-DCMAKE_CXX_FLAGS="${{CMAKE_CXX_FLAGS}} -fno-rtti"
	'source_subfolder' : '_build', #-B. -H..
	'conf_system' : 'cmake',
	# 'cpu_count' : '1', #...
	'needs_make_install' : False,
	'build_options' : '',
	# 'patches' : [
		# ('shaderc/gcc9-cast-error-workaround.patch', '-p1', '..'),
	# ],
	'run_post_patch' : [
		# 'mkdir _build',
		# 'chmod u+x pull.sh',
		# './pull.sh',
		'!SWITCHDIR|../third_party',
		'ln -sf {inTreePrefix}/glslang/ glslang',
		'ln -sf {inTreePrefix}/spirv-headers/ spirv-headers',
		'ln -sf {inTreePrefix}/spirv-tools/ spirv-tools',
		'ln -sf {inTreePrefix}/spirv-cross spirv-cross',
		'!SWITCHDIR|../_build',
		"sed -i 's/add_subdirectory(examples)/#add_subdirectory(examples)/g' ../CMakeLists.txt",
	],
	'run_post_build' : [
		'cp -rv "../libshaderc/include/shaderc" "{target_prefix}/include/"',
		'cp -rv "../libshaderc_util/include/libshaderc_util" "{target_prefix}/include/"',
		'cp -rv "libshaderc/libshaderc_combined.a" "{target_prefix}/lib/libshaderc_combined.a"',
		# 'cp -rv "libshaderc/libshaderc_combined.a" "{target_prefix}/lib/libshaderc_shared.a"',
	],
	'depends_on' : ['glslang', 'spirv-headers', 'spirv-tools', 'spirv-cross', ],
	'_info' : { 'version' : None, 'fancy_name' : 'shaderc' },
}