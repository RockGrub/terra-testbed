# New spec type dropped!! I call it THE NODE BOMB
%global srcmodule backport
%global debug_package %{nil}
## Standalone packages
%global abort_controller_ver 3.0.0
%global abort_controller_desc An implementation of WHATWG AbortController interface.
%global acorn_ver 8.14.1
%global acorn_desc ECMAScript parser
%global acorn_import_attributes_ver 1.9.5
%global acorn_import_attributes_desc Support for import attributes in acorn
%global after_all_results_ver 2.0.0
%global after_all_results_desc Bundle results of async functions calls into one callback with all the results
%global agentkeepalive_ver 4.6.0
%global agentkeepalive_desc Missing keepalive http.Agent
%global aggregate_error_ver 3.1.0
%global aggregate_error_desc Create an error from multiple errors
%global ansi_escapes_ver 4.3.2
%global ansi_escapes_desc ANSI escape codes for manipulating the terminal
%global ansi_regex_ver 5.0.1
%global ansi_regex_desc Regular expression for matching ANSI escape codes
%global ansi_styles_ver 4.3.0
%global ansi_styles_desc ANSI escape codes for styling strings in the terminal
%global array_union_ver 2.1.0
%global array_union_desc Create an array of unique values, in order, from the input arrays
%global async_ver 3.2.6
%global async_desc Higher-order functions and common patterns for asynchronous code
%global asynckit_ver 0.4.0
%global asynckit_desc Minimal async jobs utility library, with streams support
%global async_value_ver 1.2.2
%global async_value_desc Async value container
%global async_value_promise_ver 1.1.1
%global async_value_promise_desc Creates a value/error pair to mimic promise behavior
%global atomic_sleep_ver 1.0.0
%global atomic_sleep_desc Zero CPU overhead, zero dependency, true event-loop blocking sleep
%global axios_ver 1.9.0
%global axios_desc Promise based HTTP client for the browser and node.js
# Here for script reasons. I could sed it out but I want it here just in case something funny happens
%global backport_ver 9.6.6
%global backport_desc A CLI tool that automates the process of backporting commits
%global balanced_match_ver 1.0.2
%global balanced_match_desc Match balanced character pairs, like "{" and "}"
%global base64_js_ver 1.5.1
%global base64_js_desc Base64 encoding/decoding in pure JS
%global basic_auth_ver 2.0.1
%global basic_auth_desc node.js basic auth parser
%global before_after_hook_ver 2.2.3
%global before_after_hook_desc asynchronous before/error/after hooks for internal functionality
%global bignumber_js_ver 9.3.0
%global bignumber_js_desc A library for arbitrary-precision decimal and non-decimal arithmetic
%global binary_search_ver 1.3.6
%global binary_search_desc tiny binary search function with comparators
%global bl_ver 4.1.0
%global bl_desc Buffer List: collect buffers and access with a standard readable Buffer interface, streamable too!
%global brace_expansion_ver 1.1.11
%global brace_expansion_desc Brace expansion as known from sh/bash
%global braces_ver 3.0.3
%global braces_desc Bash-like brace expansion, implemented in JavaScript. Safer than other brace expansion libs, with complete support for the Bash 4.3 braces specification, without sacrificing speed.
%global breadth_filter_ver 2.0.0
%global breadth_filter_desc Breadth-first deep object filter
%global buffer_ver 5.7.1
%global buffer_desc Node.js Buffer API, for the browser
%global call_bind_ver 1.0.8
%global call_bind_desc Robustly `.call.bind()` a function
%global call_bind_apply_helpers_ver 1.0.2
%global call_bind_apply_helpers_desc Helper functions around Function call/apply/bind, for use in `call-bind`
%global call_bound_ver 1.0.4
%global call_bound_desc Robust call-bound JavaScript intrinsics, using `call-bind` and `get-intrinsic`.
%global chalk_ver 4.1.2
%global chalk_desc Terminal string styling done right
%global chardet_ver 0.7.0
%global chardet_desc Character detector
# Unused, Fedora packages this
%global cjs_module_lexer_ver 1.4.3
%global cjs_module_lexer_desc Lexes CommonJS modules, returning their named exports metadata
%global clean_stack_ver 2.2.0
%global clean_stack_desc Clean up error stack traces
%global cli_cursor_ver 3.1.0
%global cli_cursor_desc Toggle the CLI cursor
%global cli_spinners_ver 2.9.2
%global cli_spinners_desc Spinners for use in the terminal
%global cliui_ver 8.0.1
%global cliui_desc easily create complex multi-column command-line-interfaces
%global cli_width_ver 3.0.0
%global cli_width_desc Get stdout window width, with two fallbacks, tty and then a default.
%global clone_ver 1.0.4
%global clone_desc deep cloning of objects and arrays
%global color_ver 3.2.1
%global color_desc Color conversion and manipulation with CSS string support
%global color_convert_ver 2.0.1
%global color_convert_desc Plain color conversion functions
%global color_name_ver 1.1.4
%global color_name_desc A list of color names and its values
%global colorspace_ver 1.1.4
%global colorspace_desc Generate HEX colors for a given namespace.
%global color_string_ver 1.9.1
%global color_string_desc Parser and generator for CSS color strings
%global combined_stream_ver 1.0.8
%global combined_stream_desc A stream that emits multiple other streams one after another.
%global concat_map_ver 
%global concat_map_desc The NodeJS concat-map package
%global console_log_level_ver 1.4.1
%global console_log_level_desc The most simple logger imaginable
%global cookie_ver 0.7.2
%global cookie_desc HTTP server cookie parsing and serialization
%global core_util_is_ver 1.0.3
%global core_util_is_desc The `util.is*` functions introduced in Node v0.12.
%global debug_ver 4.4.1
%global debug_desc Lightweight debugging utility for Node.js and the browser
%global dedent_ver 0.7.0
%global dedent_desc An ES6 string tag that strips indentation from multi-line strings
%global defaults_ver 1.0.4
%global defaults_desc merge single level defaults over a config object
%global define_data_property_ver 1.1.4
%global define_data_property_desc Define a data property on an object. Will fall back to assignment in an engine without descriptors.
%global define_properties_ver 1.2.1
%global define_properties_desc Define multiple non-enumerable properties at once. Uses `Object.defineProperty` when available; falls back to standard assignment in older engines.
%global del_ver 6.1.1
%global del_desc Delete files and directories
%global delayed_stream_ver 1.0.0
%global delayed_stream_desc Buffers events from a stream until you are ready to handle them.
%global deprecation_ver 2.3.1
%global deprecation_desc Log a deprecation message with stack
%global dir_glob_ver 3.0.1
%global dir_glob_desc Convert directories to glob compatible strings
%global dotenv_ver 16.5.0
%global dotenv_desc Loads environment variables from .env file
%global dunder_proto_ver 1.0.1
%global dunder_proto_desc If available, the `Object.prototype.__proto__` accessor and mutator, call-bound
%global elastic_apm_node_ver 4.13.0
%global elastic_apm_node_desc The official Elastic APM agent for Node.js
%global emoji_regex_ver 8.0.0
%global emoji_regex_desc A regular expression to match all Emoji-only symbols as per the Unicode Standard.
%global enabled_ver 2.0.0
%global enabled_desc Check if a certain debug flag is enabled.
%global end_of_stream_ver 1.4.4
%global end_of_stream_desc Call a callback when a readable/writable/duplex stream has completed or failed.
%global error_callsites_ver 2.0.4
%global error_callsites_desc Extract callsite objects from Error objects
%global error_stack_parser_ver 2.1.4
%global error_stack_parser_desc Extract meaning from JS Errors
%global escalade_ver 3.2.0
%global escalade_desc A tiny (183B to 210B) and fast utility to ascend parent directories
%global escape_string_regexp_ver 4.0.0
%global escape_string_regexp_desc Escape RegExp special characters
%global es_define_property_ver 1.0.1
%global es_define_property_desc `Object.defineProperty`, but not IE 8's broken one.
%global es_errors_ver 1.3.0
%global es_errors_desc A simple cache for a few of the JS Error constructors.
%global es_object_atoms_ver 1.1.1
%global es_object_atoms_desc ES Object-related atoms: Object, ToObject, RequireObjectCoercible
%global es_set_tostringtag_ver 2.1.0
%global es_set_tostringtag_desc A helper to optimistically set Symbol.toStringTag, when possible.
%global events_ver 3.3.0
%global events_desc Node's event emitter for all engines.
%global event_target_shim_ver 5.0.1
%global event_target_shim_desc An implementation of WHATWG EventTarget interface.
%global external_editor_ver 3.1.0
%global external_editor_desc Edit a string with the users preferred text editor using $VISUAL or $ENVIRONMENT
%global fast_glob_ver 3.3.3
%global fast_glob_desc It's a very fast and efficient glob library for Node.js
%global fastq_ver 1.19.1
%global fastq_desc Fast, in memory work queue
%global fast_redact_ver 3.5.0
%global fast_redact_desc very fast object redaction
%global fast_safe_stringify_ver 2.1.1
%global fast_safe_stringify_desc Safely and quickly serialize JavaScript objects
%global fast_stream_to_buffer_ver 1.0.0
%global fast_stream_to_buffer_desc Consume a stream of data into a binary Buffer as efficiently as possible
%global fecha_ver 4.2.3
%global fecha_desc Date formatting and parsing
%global figures_ver 3.2.0
%global figures_desc Unicode symbols with Windows CMD fallbacks
%global fill_range_ver 7.1.1
%global fill_range_desc Fill in a range of numbers or letters, optionally passing an increment or `step` to use, or create a regex-compatible range with `options.toRegex`
%global find_up_ver 5.0.0
%global find_up_desc Find a file or directory by walking up parent directories
%global fn_name_ver 1.1.0
%global fn_name_desc Extract names from functions
%global follow_redirects_ver 1.15.9
%global follow_redirects_desc HTTP and HTTPS modules that follow redirects.
%global form_data_ver 4.0.2
%global form_data_desc A library to create readable "multipart/form-data" streams. Can be used to submit forms and file uploads to other web applications.
%global forwarded_parse_ver 2.1.2
%global forwarded_parse_desc Parse the Forwarded header (RFC 7239) into an array of objects
%global fs_realpath_ver 1.0.0
%global fs_realpath_desc Use node's fs.realpath, but fall back to the JS implementation if the native one fails
%global function_bind_ver 1.1.2
%global function_bind_desc Implementation of Function.prototype.bind
%global get_caller_file_ver 2.0.5
%global get_caller_file_desc The NodeJS get-caller-file package
%global get_intrinsic_ver 1.3.0
%global get_intrinsic_desc Get and robustly cache all JS language-level intrinsics at first require time
%global get_proto_ver 1.0.1
%global get_proto_desc Robustly get the [[Prototype]] of an object
%global glob_ver 7.2.3
%global glob_desc a little globber
%global globby_ver 11.1.0
%global globby_desc User-friendly glob matching
%global glob_parent_ver 5.1.2
%global glob_parent_desc Extract the non-magic parent path from a glob string.
%global gopd_ver 1.2.0
%global gopd_desc `Object.getOwnPropertyDescriptor`, but accounts for IE's broken implementation.
%global graceful_fs_ver 4.2.11
%global graceful_fs_desc A drop-in replacement for fs, making various improvements.
%global graphql_ver 16.11.0
%global graphql_desc A Query Language and Runtime which can target any service.
%global graphql_tag_ver 2.12.6
%global graphql_tag_desc A JavaScript template literal tag that parses GraphQL queries
%global handlebars_ver 4.7.8
%global handlebars_desc Handlebars provides the power necessary to let you build semantic templates effectively with no frustration
%global has_flag_ver 4.0.0
%global has_flag_desc Check if argv has a specific flag
%global hasown_ver 2.0.2
%global hasown_desc A robust, ES3 compatible, "has own property" predicate.
%global has_property_descriptors_ver 1.0.2
%global has_property_descriptors_desc Does the environment have full property descriptor support? Handles IE 8's broken defineProperty/gOPD.
%global has_symbols_ver 1.1.0
%global has_symbols_desc Determine if the JS environment has Symbol support. Supports spec, or shams.
%global has_tostringtag_ver 1.0.2
%global has_tostringtag_desc Determine if the JS environment has `Symbol.toStringTag` support. Supports spec, or shams.
%global http_headers_ver 3.0.2
%global http_headers_desc Parse http headers
%global humanize_ms_ver 1.2.1
%global humanize_ms_desc transform humanize time to ms
%global iconv_lite_ver 0.4.24
%global iconv_lite_desc Convert character encodings in pure javascript.
%global ieee754_ver 1.2.1
%global ieee754_desc Read/write IEEE754 floating point numbers from/to a Buffer or array-like object
%global ignore_ver 5.3.2
%global ignore_desc Ignore is a manager and filter for .gitignore rules, the one used by eslint, gitbook and many others.
%global import_in_the_middle_ver 1.13.1
%global import_in_the_middle_desc Intercept imports in Node.js
%global indent_string_ver 4.0.0
%global indent_string_desc Indent each line in a string
%global inflight_ver 1.0.6
%global inflight_desc Add callbacks to requests in flight to avoid async duplication
%global inherits_ver 2.0.4
%global inherits_desc Browser-friendly inheritance fully compatible with standard node.js inherits()
%global inquirer_ver 8.2.6
%global inquirer_desc A collection of common interactive command line user interfaces.
%global is_arrayish_ver 0.3.2
%global is_arrayish_desc Determines if an object can be used as an array
%global is_core_module_ver 2.16.1
%global is_core_module_desc Is this specifier a node.js core module?
%global is_extglob_ver 2.1.1
%global is_extglob_desc Returns true if a string has an extglob.
%global is_finite_ver 1.1.0
%global is_finite_desc ES2015 Number.isFinite() ponyfill
%global is_fullwidth_code_point_ver 3.0.0
%global is_fullwidth_code_point_desc Check if the character represented by a given Unicode code point is fullwidth
%global is_glob_ver 4.0.3
%global is_glob_desc Returns `true` if the given string looks like a glob pattern or an extglob pattern. This makes it easy to create code that only uses external modules like node-glob when necessary, resulting in much faster code execution and initialization time, and a better user experience.
%global is_integer_ver 1.0.7
%global is_integer_desc ES2015 (ES6) Number.isInteger polyfill
%global is_interactive_ver 1.0.0
%global is_interactive_desc Check if stdout or stderr is interactive
%global is_number_ver 7.0.0
%global is_number_desc Returns true if a number or string value is a finite number. Useful for regex matches, parsing, user input, etc.
%global is_path_cwd_ver 2.2.0
%global is_path_cwd_desc Check if a path is the current working directory
%global is_path_inside_ver 3.0.3
%global is_path_inside_desc Check if a path is inside another path
%global is_plain_object_ver 5.0.0
%global is_plain_object_desc Returns true if an object was created by the `Object` constructor, or Object.create(null).
%global is_stream_ver 2.0.1
%global is_stream_desc Check if something is a Node.js stream
%global is_unicode_supported_ver 0.1.0
%global is_unicode_supported_desc Detect whether the terminal supports Unicode
%global json_bigint_ver 1.0.0
%global json_bigint_desc JSON.parse with bigints support
%global kuler_ver 2.0.0
%global kuler_desc Color your terminal using CSS/hex color codes
%global locate_path_ver 6.0.0
%global locate_path_desc Get the first path that exists on disk of multiple paths
%global lodash_ver 4.17.21
%global lodash_desc Lodash modular utilities.
%global lodash_sortby_ver 4.7.0
%global lodash_sortby_desc The lodash method `_.sortBy` exported as a module.
%global logform_ver 2.7.0
%global logform_desc An mutable object-based log format designed for chaining & objectMode streams.
%global log_symbols_ver 4.1.0
%global log_symbols_desc Colored symbols for various log levels. Example: `✔︎ Success`
%global lru_cache_ver 10.2.0
%global lru_cache_desc A cache object that deletes the least-recently-used items.
%global make_dir_ver 3.1.0
%global make_dir_desc Make a directory and its parents if needed - Think `mkdir -p`
%global mapcap_ver 1.0.0
%global mapcap_desc Apply a size limit to a Map class or instance
%global math_intrinsics_ver 1.1.0
%global math_intrinsics_desc ES Math-related intrinsics and helpers, robustly cached.
%global measured_core_ver 1.51.1
%global measured_core_desc A Node library for measuring and reporting application-level metrics.
%global measured_reporting_ver 1.51.1
%global measured_reporting_desc The classes needed to create self reporting dimension aware metrics registries
%global merge2_ver 1.4.1
%global merge2_desc Merge multiple streams into one stream in sequence or parallel.
%global micromatch_ver 4.0.8
%global micromatch_desc Glob matching for javascript/node.js. A replacement and faster alternative to minimatch and multimatch.
%global mime_db_ver 1.52.0
%global mime_db_desc Media Type Database
%global mime_types_ver 2.1.35
%global mime_types_desc The ultimate javascript content-type utility.
%global mimic_fn_ver 2.1.0
%global mimic_fn_desc Make a function mimic another one
%global minimatch_ver 3.1.2
%global minimatch_desc a glob matcher in javascript
%global minimist_ver 1.2.8
%global minimist_desc parse argument options
%global module_details_from_path_ver 1.0.4
%global module_details_from_path_desc Resolve npm package details, like name and base path, given an absolute path to a file inside a package
%global monitor_event_loop_delay_ver 1.0.0
%global monitor_event_loop_delay_desc Polyfill for perf_hooks.monitorEventLoopDelay(...)
%global ms_ver 2.1.3
%global ms_desc Tiny millisecond conversion utility
%global mute_stream_ver 0.0.8
%global mute_stream_desc Bytes go in, but they don't come out (when muted).
%global neo_async_ver 2.6.2
%global neo_async_desc Neo-Async is a drop-in replacement for Async, it almost fully covers its functionality and runs faster 
%global next_line_ver 1.1.0
%global next_line_desc Iterator over lines in a string
%global node_fetch_ver 2.7.0
%global node_fetch_desc A light-weight module that brings window.fetch to node.js
%global object_entries_ver 1.1.9
%global object_entries_desc ES2017 spec-compliant Object.entries shim.
%global object_filter_sequence_ver 1.0.0
%global object_filter_sequence_desc Apply a sequence of filter functions to an object
%global object_identity_map_ver 1.0.2
%global object_identity_map_desc Map implementation based on object identity
%global object_keys_ver 1.1.1
%global object_keys_desc An Object.keys replacement, in case Object.keys is not available. From https://github.com/es-shims/es5-shim
%global once_ver 1.4.0
%global once_desc Run a function exactly one time
%global one_time_ver 1.0.0
%global one_time_desc Run the supplied function exactly one time (once)
%global onetime_ver 5.1.2
%global onetime_desc Ensure a function is only called once
%global on_exit_leak_free_ver 2.1.2
%global on_exit_leak_free_desc Execute a function on exit without leaking memory, allowing all objects to be garbage collected
%global optional_js_ver 2.3.0
%global optional_js_desc Optionals for JS - wrapper for possibly undefined values, inspired by Java Optional API
%global ora_ver 5.4.1
%global ora_desc Elegant terminal spinner
%global original_url_ver 1.2.3
%global original_url_desc Reconstruct the original URL used in an HTTP request based on the HTTP request headers
%global os_tmpdir_ver 1.0.2
%global os_tmpdir_desc Node.js os.tmpdir() ponyfill
%global path_exists_ver 4.0.0
%global path_exists_desc Check if a path exists
%global path_is_absolute_ver 1.0.1
%global path_is_absolute_desc Node.js 0.12 path.isAbsolute() ponyfill
%global path_parse_ver 1.0.7
%global path_parse_desc Node.js path.parse() ponyfill
%global path_type_ver 4.0.0
%global path_type_desc Check if a path is a file, directory, or symlink
%global picomatch_ver 2.3.1
%global picomatch_desc Blazing fast and accurate glob matcher written in JavaScript, with no dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions.
%global pino_ver 8.21.0
%global pino_desc super fast, all natural json logger
%global pino_abstract_transport_ver 1.2.0
%global pino_abstract_transport_desc Write Pino transports easily
%global pino_std_serializers_ver 6.2.2
%global pino_std_serializers_desc A collection of standard object serializers for Pino
%global p_limit_ver 3.1.0
%global p_limit_desc Run multiple promise-returning & async functions with limited concurrency
%global p_locate_ver 5.0.0
%global p_locate_desc Get the first fulfilled promise that satisfies the provided testing function
%global p_map_ver 4.0.0
%global p_map_desc Map over promises concurrently
%global process_ver 0.11.10
%global process_desc process information for node.js and browsers
%global process_warning_ver 3.0.0
%global process_warning_desc A small utility for creating warnings and emitting them.
%global proxy_from_env_ver 1.1.0
%global proxy_from_env_desc Offers getProxyForUrl to get the proxy URL for a URL, respecting the *_PROXY (e.g. HTTP_PROXY) and NO_PROXY environment variables.
%global punycode_ver 2.3.1
%global punycode_desc A robust Punycode converter that fully complies to RFC 3492 and RFC 5891, and works on nearly all JavaScript platforms.
%global queue_microtask_ver 1.2.3
%global queue_microtask_desc fast, tiny `queueMicrotask` shim for modern engines
%global quick_format_unescaped_ver 4.0.4
%global quick_format_unescaped_desc Solves a problem with util.format
%global readable_stream_ver 3.6.2
%global readable_stream_desc Streams3, a user-land copy of the stream library from Node.js
%global real_require_ver 0.2.0
%global real_require_desc Keep require and import consistent after bundling or transpiling
%global relative_microtime_ver 2.0.0
%global relative_microtime_desc Get the number of microseconds elapsed since January 1, 1970 00:00:00 UTC without fear of clock drift
%global require_directory_ver 2.1.1
%global require_directory_desc Recursively iterates over specified directory, require()'ing each file, and returning a nested hash structure containing those modules.
%global require_in_the_middle_ver 7.5.2
%global require_in_the_middle_desc Module to hook into the Node.js require function
%global resolve_ver 1.22.10
%global resolve_desc resolve like require.resolve() on behalf of files asynchronously and synchronously
%global restore_cursor_ver 3.1.0
%global restore_cursor_desc Gracefully restore the CLI cursor on exit
%global reusify_ver 1.1.0
%global reusify_desc Reuse objects and functions with style
%global rimraf_ver 3.0.2
%global rimraf_desc A deep deletion module for node (like `rm -rf`)
%global run_async_ver 2.4.1
%global run_async_desc Utility method to run function either synchronously or asynchronously using the common `this.async()` style.
%global run_parallel_ver 1.2.0
%global run_parallel_desc Run an array of functions in parallel
%global rxjs_ver 7.8.2
%global rxjs_desc Reactive Extensions for modern JavaScript
%global safe_buffer_ver 5.1.2
%global safe_buffer_desc Safer Node.js Buffer API
%global safe_json_stringify_ver 1.2.0
%global safe_json_stringify_desc Prevent defined property getters from throwing errors
%global safer_buffer_ver 2.1.2
%global safer_buffer_desc Modern Buffer API polyfill without footguns
%global safe_stable_stringify_ver 2.5.0
%global safe_stable_stringify_desc Deterministic and safely JSON.stringify to quickly serialize JavaScript objects
%global semver_ver 7.7.2
%global semver_desc The semantic version parser used by npm.
%global set_function_length_ver 1.2.2
%global set_function_length_desc Set a function's length property
%global shallow_clone_shim_ver 2.0.0
%global shallow_clone_shim_desc Shallow clones an object while respecting the original property descriptors
%global signal_exit_ver 3.0.7
%global signal_exit_desc when you want to fire an event no matter how a process exits.
%global simple_swizzle_ver 0.2.2
%global simple_swizzle_desc Simply swizzle your arguments
%global slash_ver 3.0.0
%global slash_desc Convert Windows backslash paths to slash paths
%global sonic_boom_ver 3.8.1
%global sonic_boom_desc Extremely fast utf8 only stream implementation
%global source_map_ver 0.8.0~beta.0
%global source_map_desc Generates and consumes source maps
%global split2_ver 4.2.0
%global split2_desc split a Text Stream into a Line Stream, using Stream 3
%global sql_summary_ver 1.0.1
%global sql_summary_desc Summarize any SQL query
%global stackframe_ver 1.3.4
%global stackframe_desc JS Object representation of a stack frame
%global stack_trace_ver 0.0.10
%global stack_trace_desc Get v8 stack traces as an array of CallSite objects.
%global stream_chopper_ver 3.0.1
%global stream_chopper_desc Chop a single stream of data into a series of readable streams
%global string_decoder_ver 1.3.0
%global string_decoder_desc The string_decoder module from Node core
%global string_width_ver 4.2.3
%global string_width_desc Get the visual width of a string - the number of columns required to display it
%global strip_ansi_ver 6.0.1
%global strip_ansi_desc Strip ANSI escape codes from a string
%global strip_json_comments_ver 3.1.1
%global strip_json_comments_desc Strip comments from JSON. Lets you use comments in your JSON files!
%global supports_color_ver 7.2.0
%global supports_color_desc Detect whether a terminal supports color
%global supports_hyperlinks_ver 2.3.0
%global supports_hyperlinks_desc Detect if your terminal emulator supports hyperlinks
%global supports_preserve_symlinks_flag_ver 1.0.0
%global supports_preserve_symlinks_flag_desc Determine if the current node version supports the `--preserve-symlinks` flag.
%global terminal_link_ver 2.1.1
%global terminal_link_desc Create clickable links in the terminal
%global text_hex_ver 1.0.0
%global text_hex_desc Generate a hex color from the given text
%global thread_stream_ver 2.7.0
%global thread_stream_desc A streaming way to send data to a Node.js Worker Thread
%global through_ver 2.3.8
%global through_desc simplified stream construction
%global tmp_ver 0.0.33
%global tmp_desc Temporary file and directory creator
%global to_regex_range_ver 5.0.1
%global to_regex_range_desc Pass two numbers, get a regex-compatible source string for matching ranges. Validated against more than 2.78 million test assertions.
%global tr46_ver 0.0.3
%global tr46_desc An implementation of the Unicode TR46 spec
%global triple_beam_ver 1.4.1
%global triple_beam_desc Definitions of levels for logging purposes & shareable Symbol constants.
%global tslib_ver 2.8.1
%global tslib_desc Runtime library for TypeScript helper functions
%global type_fest_ver 0.21.3
%global type_fest_desc A collection of essential TypeScript types
# Unused, Fedora packages this
%global uglify_js_ver 3.19.3
%global uglify_js_desc JavaScript parser, mangler/compressor and beautifier toolkit
%global unicode_byte_truncate_ver 1.0.0
%global unicode_byte_truncate_desc Unicode aware string truncation that given a max byte size will truncate the string to or just below that size
%global unicode_substring_ver 0.1.0
%global unicode_substring_desc Unicode-aware substring
%global universal_user_agent_ver 6.0.1
%global universal_user_agent_desc Get a user agent string in both browser and node
%global util_deprecate_ver 1.0.2
%global util_deprecate_desc The Node.js `util.deprecate()` function with browser support
%global utility_types_ver 3.11.0
%global utility_types_desc Utility Types Collection for TypeScript
%global wcwidth_ver 1.0.1
%global wcwidth_desc Port of C's wcwidth() and wcswidth()
%global webidl_conversions_ver 3.0.1
%global webidl_conversions_desc Implements the WebIDL algorithms for converting to and from JavaScript values
%global whatwg_url_ver 5.0.0
%global whatwg_url_desc An implementation of the WHATWG URL Standard's URL API and parsing machinery
%global winston_ver 3.17.0
%global winston_desc A logger for just about everything.
%global winston_transport_ver 4.9.0
%global winston_transport_desc Base stream implementations for winston@3 and up.
%global wordwrap_ver 1.0.0
%global wordwrap_desc Wrap those words. Show them at what columns to start and stop.
%global wrap_ansi_ver 6.2.0
%global wrap_ansi_desc Wordwrap a string with ANSI escape codes
%global wrappy_ver 1.0.2
%global wrappy_desc Callback wrapping utility
%global y18n_ver 5.0.8
%global y18n_desc the bare-bones internationalization library used by yargs
%global yargs_ver 17.7.2
%global yargs_desc yargs the modern, pirate-themed, successor to optimist.
%global yargs_parser_ver 21.1.1
%global yargs_parser_desc the mighty option parser used by yargs
%global yocto_queue_ver 0.1.0
%global yocto_queue_desc Tiny queue data structure
## Grouped packages
%global colors_colors_ver 1.6.0
%global colors_colors_desc get colors in your node.js console
%global dabh_diagnostics_ver 2.0.3
%global dabh_diagnostics_desc Tools for debugging your node.js modules and event loop
%global elastic_ecs_helpers_ver 2.1.1
%global elastic_ecs_helpers_desc ecs-logging-nodejs helpers
%global elastic_ecs_pino_format_ver 1.5.0
%global elastic_ecs_pino_format_desc A formatter for the pino logger compatible with Elastic Common Schema.
%global nodelib_fs_scandir_ver 2.1.5
%global nodelib_fs_scandir_desc List files and directories inside the specified directory
%global nodelib_fs_stat_ver 2.0.5
%global nodelib_fs_stat_desc Get the status of a file with some features
%global nodelib_fs_walk_ver 1.2.8
%global nodelib_fs_walk_desc A library for efficiently walking a directory recursively
%global octokit_auth_token_ver 3.0.4
%global octokit_auth_token_desc GitHub API token authentication for browsers and Node.js
%global octokit_core_ver 4.2.4
%global octokit_core_desc Extendable client for GitHub's REST & GraphQL APIs
%global octokit_endpoint_ver 7.0.6
%global octokit_endpoint_desc Turns REST API endpoints into generic request options
%global octokit_graphql_ver 5.0.6
%global octokit_graphql_desc GitHub GraphQL API client for browsers and Node
%global octokit_openapi_types_ver 18.1.1
%global octokit_openapi_types_desc Generated TypeScript definitions based on GitHub's OpenAPI spec for api.github.com
%global octokit_plugin_paginate_rest_ver 6.1.2
%global octokit_plugin_paginate_rest_desc Octokit plugin to paginate REST API endpoint responses
%global octokit_plugin_request_log_ver 1.0.4
%global octokit_plugin_request_log_desc Log all requests and request errors
%global octokit_plugin_rest_endpoint_methods_ver 7.2.3
%global octokit_plugin_rest_endpoint_methods_desc Octokit plugin adding one method for all of api.github.com REST API endpoints
%global octokit_request_ver 6.2.8
%global octokit_request_desc Send parameterized requests to GitHub's APIs with sensible defaults in browsers and Node
%global octokit_request_error_ver 3.0.3
%global octokit_request_error_desc Error class for Octokit request errors
%global octokit_rest_ver 19.0.13
%global octokit_rest_desc GitHub REST API client for Node.js
%global octokit_tsconfig_ver 1.0.2
%global octokit_tsconfig_desc TypeScript configuration for Octokit packages
%global octokit_types_ver 9.3.2
%global octokit_types_desc Shared TypeScript definitions for Octokit projects
%global opentelemetry_api_ver 1.9.0
%global opentelemetry_api_desc Public API for OpenTelemetry
%global opentelemetry_core_ver 1.30.1
%global opentelemetry_core_desc OpenTelemetry Core provides constants and utilities shared by all OpenTelemetry SDK packages.
%global opentelemetry_resources_ver 1.30.1
%global opentelemetry_resources_desc OpenTelemetry SDK resources
%global opentelemetry_sdk_metrics_ver 1.30.1
%global opentelemetry_sdk_metrics_desc OpenTelemetry metrics SDK
%global opentelemetry_semantic_conventions_ver 1.28.0
%global opentelemetry_semantic_conventions_desc OpenTelemetry semantic conventions
%global types_triple_beam_ver 1.3.5
%global types_triple_beam_desc TypeScript definitions for triple-beam
%dnl %bcond test 0

Name:          node-%{srcmodule}
Version:       9.6.6
Release:       1%{?dist}
Summary:       Backport GitHub commits
License:       Apache-2.0 AND
URL:           https://github.com/sorenlouv/backport
%dnl Source0:       http://registry.npmjs.org/%{srcmodule}/-/%{srcmodule}-%{version}.tgz
Source0:       %{srcmodule}-%{version}.tar.gz
# Source the tests
Source1:       tests-%{version}.tar.bz2
BuildRequires: binutils
BuildRequires: bsdtar
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: uglify-js
BuildRequires: web-assets-devel
ExclusiveArch: %{nodejs_arches} noarch

%description
A simple CLI tool that automates the process of backporting commits on a GitHub repo.

%package -n     nodejs-%{srcmodule}
Summary:        Backport GitHub commits
License:        Apache-2.0
BuildArch:      noarch

%description -n nodejs-%{srcmodule}
%{backport_desc}

%package -n     nodejs-abort-controller
Version:        %{abort_controller_ver}
Summary:        The NodeJS abort-controller package
License:        MIT
BuildArch:      noarch

%description -n nodejs-abort-controller
%{abort_controller_desc}

%package -n     nodejs-acorn
Version:        %{acorn_ver}
Summary:        The NodeJS acorn package
License:        MIT
BuildArch:      noarch

%description -n nodejs-acorn
%{acorn_desc}

%package -n     nodejs-acorn-import-attributes
Version:        %{acorn_import_attributes_ver}
Summary:        The NodeJS acorn-import-attributes package
License:        MIT
BuildArch:      noarch

%description -n nodejs-acorn-import-attributes
%{acorn_import_attributes_desc}

%package -n     nodejs-after-all-results
Version:        %{after_all_results_ver}
Summary:        The NodeJS after-all-results package
License:        MIT
BuildArch:      noarch

%description -n nodejs-after-all-results
%{after_all_results_desc}

%package -n     nodejs-agentkeepalive
Version:        %{agentkeepalive_ver}
Summary:        The NodeJS agentkeepalive package
License:        MIT
BuildArch:      noarch

%description -n nodejs-agentkeepalive
%{agentkeepalive_desc}

%package -n     nodejs-aggregate-error
Version:        %{aggregate_error_ver}
Summary:        The NodeJS aggregate-error package
License:        MIT
BuildArch:      noarch

%description -n nodejs-aggregate-error
%{aggregate_error_desc}

%package -n     nodejs-ansi-escapes
Version:        %{ansi_escapes_ver}
Summary:        The NodeJS ansi-escapes package
License:        MIT
BuildArch:      noarch

%description -n nodejs-ansi-escapes
%{ansi_escapes_desc}

%package -n     nodejs-ansi-regex
Version:        %{ansi_regex_ver}
Summary:        The NodeJS ansi-regex package
License:        MIT
BuildArch:      noarch

%description -n nodejs-ansi-regex
%{ansi_regex_desc}

%package -n     nodejs-ansi-styles
Version:        %{ansi_styles_ver}
Summary:        The NodeJS ansi-styles package
License:        MIT
BuildArch:      noarch

%description -n nodejs-ansi-styles
%{ansi_styles_desc}

%package -n     nodejs-array-union
Version:        %{array_union_ver}
Summary:        The NodeJS array-union package
License:        MIT
BuildArch:      noarch

%description -n nodejs-array-union
%{array_union_desc}

%package -n     js-async
Version:        %{async_ver}
Summary:        The JS async package
License:        MIT
Requires:       nodejs-async = %{async_ver}-%{release}
BuildArch:      noarch

%description -n js-async
%{async_desc}

%package -n     nodejs-async
Version:        %{async_ver}
Summary:        NodeJS compatibility package for async
License:        MIT
Requires:       js-async = %{async_ver}-%{release}
BuildArch:      noarch

%description -n nodejs-async
%{async_desc}

%package -n     js-async-value

%prep
%autosetup -n %{srcmodule}/node_modules/%{srcmodule}
tar xjf %{SOURCE1}

# Remove packages Fedora provides
rm -rf node_modules/{cjs-module-lexer,uglify-js}

%build
# Empty build section, because RPM reasons

%install
mkdir -p %{buildroot}%{nodejs_sitelib}
mkdir -p %{buildroot}%{nodejs_sitearch}
mkdir -p %{buildroot}%{_bindir}

# Async and async-value are pure JS packages, move them ahead of time
mkdir -p %{buildroot}%{_jsdir}
pushd node_modules/async/dist
rm async.min.js
uglifyjs async.js -o async.min.js
popd
mv node_modules/async -t %{buildroot}%{_jsdir}
# Compatibility symlink for NodeJS packages
mkdir -p %{buildroot}%{nodejs_sitelib}/async/dist
ln -sf %{_jsdir}/async/dist/async.js %{buildroot}%{nodejs_sitelib}/async/dist/async.js

## Explaining the process of these horrible loops, in order:
# Uglify the JS packages per Fedora packaging standards if they exist (I don't know why they do this?)
# Account for the different names the *min.js file can have
# If Uglify fails, restore original files; if it succeeds, toss the original files in the bin
# Move the JS package components to the JS dir
# Check if the NodeJS packages have executables
# If they do, check if they are binary or scripts
# Install accordingly
# Symlink all executables to the /usr/bin folder so they are in the $PATH
# Tada, mostly Fedora compliant mass NodeJS packages!!
# Note: "@node" packages are grouped packages, they must be kept together and are therefore handled slightly differently
# All of this to avoid bundled deps...

for node in $(ls node_modules | sed '/^\@.*/d'); do
  if [[ $(stat node_modules/$node/${node}.js) ]]; then
   mkdir -p %{buildroot}%{_jsdir}/$node
   pushd node_modules/$node
   if [[ $(stat ${node}-min.js) ]]; then
     mv ${node}-min.js ${node}-min.js.bak
     uglifyjs $node.js -o ${node}-min.js || mv ${node}-min.js.bak ${node}-min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
     mv ${node}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$node
   elif [[ $(stat ${node}.min.js) ]]; then
     mv ${node}.min.js ${node}.min.js.bak
     uglifyjs $node.js -o ${node}.min.js || mv ${node}.min.js.bak ${node}.min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
     mv ${node}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$node
   fi
   mv ${node}.js -t %{buildroot}%{_jsdir}/$node
   ln -sf %{_jsdir}/$node/$node.js $node.js
   popd
  elif [[ $(stat node_modules/$node/lib/${node}.js) ]]; then
    mkdir -p %{buildroot}%{_jsdir}/$node
    pushd node_modules/$node/lib
    if [[ $(stat ${node}-min.js) ]]; then
     mv ${node}-min.js ${node}-min.js.bak
     uglifyjs $node.js -o ${node}-min.js || mv ${node}-min.js.bak ${node}-min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
     mv ${node}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$node
   elif [[ $(stat ${node}.min.js) ]]; then
     mv ${node}.min.js ${node}.min.js.bak
     uglifyjs $node.js -o ${node}.min.js || mv ${node}.min.js.bak ${node}.min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
     mv ${node}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$node
    fi
    mv ${node}.js -t %{buildroot}%{_jsdir}/$node
    ln -sf %{_jsdir}/$node/$node.js $node.js
    popd
  fi
   if [[ $(stat node_modules/$node/bin/$node) ]]; then
     if [[ $(readelf -h node_modules/$node/bin/$node 2>/dev/null) ]]; then
       cp -pr node_modules/$node %{buildroot}%{nodejs_sitearch}/$node
       ln -sf %{nodejs_sitearch}/$node/bin/$node %{buildroot}%{_bindir}/$node
     else
       cp -pr node_modules/$node %{buildroot}%{nodejs_sitelib}/$node
       ln -sf %{nodejs_sitelib}/$node/bin/$node %{buildroot}%{_bindir}/$node
     fi
   else
   cp -pr node_modules/$node %{buildroot}%{nodejs_sitelib}/$node
  fi
done

for atnode in $(ls node_modules | grep '@'); do
   for subnode in $(ls node_modules/$atnode); do
    if [[ $(stat node_modules/$atnode/$subnode/${subnode}.js) ]]; then
      mkdir -p %{buildroot}%{_jsdir}/$atnode/$subnode
      pushd node_modules/$atnode/$subnode
     if [[ $(stat ${subnode}-min.js) ]]; then
     mv ${subnode}-min.js ${subnode}-min.js.bak
     uglifyjs $subnode.js -o ${subnode}-min.js || mv ${subnode}-min.js.bak ${subnode}-min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
     mv ${subnode}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$atnode/$subnode
   elif [[ $(stat ${subnode}.min.js) ]]; then
     mv ${subnode}.min.js ${subnode}.min.js.bak
     uglifyjs $subnode.js -o ${subnode}.min.js || mv ${subnode}.min.js.bak ${subnode}.min.js
     if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
      mv ${subnode}.js -t %{buildroot}%{_jsdir}/$atnode/$subnode
      ln -sf %{_jsdir}/$atnode/$subnode/$subnode.js $subnode.js
      popd
    elif [[ $(stat node_modules/$atnode/$subnode/lib/${subnode}.js) ]]; then
      mkdir -p %{buildroot}%{_jsdir}/$atnode/$subnode || :
      pushd node_modules/$atnode/$subnode/lib
      if [[ $(stat ${subnode}-min.js) ]]; then
      mv ${subnode}-min.js ${subnode}-min.js.bak
      uglifyjs $subnode.js -o ${subnode}-min.js || mv ${subnode}-min.js.bak ${subnode}-min.js
      if [ $(stat *.bak) ]]; then
      rm *.bak
      fi
      mv ${subnode}*{min.js,.map*} -t %{buildroot}%{_jsdir}/$atnode/$subnode
   elif [[ $(stat ${subnode}.min.js) ]]; then
      mv ${subnode}.min.js ${subnode}.min.js.bak
      uglifyjs $subnode.js -o ${subnode}.min.js || mv ${subnode}.min.js.bak ${subnode}.min.js
      if [ $(stat *.bak) ]]; then
      rm *.bak
     fi
      mv ${subnode}*{.js,.map*} -t %{buildroot}%{_jsdir}/$atnode/$subnode
      ln -sf %{_jsdir}/$atnode/$subnode/$subnode.js $subnode.js
      popd
    fi
     if [[ $(stat node_modules/$atnode/$subnode/bin/$subnode) ]]; then
       if [[ $(readelf -h node_modules/$atnode/$subnode/bin/$subnode 2>/dev/null) ]]; then
         mkdir -p %{buildroot}%{nodejs_sitearch}/$atnode || :
         cp -pr node_modules/$atnode/$subnode %{buildroot}%{nodejs_sitearch}/$atnode/$subnode
         ln -sf %{nodejs_sitearch}/$atnode/$subnode/bin/$subnode %{buildroot}%{_bindir}/$subnode
       else
         mkdir -p %{nodejs_sitelib}/$atnode || :
         cp -pr node_modules/$atnode/$subnode %{buildroot}%{nodejs_sitelib}/$atnode/$subnode
         ln -sf %{nodejs_sitelib}/$atnode/$subnode/bin/$subnode %{buildroot}%{_bindir}/$subnode
       fi
     else
       cp -pr node_modules/$atnode %{buildroot}%{nodejs_sitelib}/$atnode
       ln -sf  %{nodejs_sitelib}/$atnode/$subnode/bin/$subnode %{buildroot}%{_bindir}/$subnode
     fi
   done
done

# Remove the symlinks for packages that do not have executables/scripts
#rm -rf %{buildroot}%{_bindir}/{abort-controller,acorn-import-attributes,after-all-results,agentkeepalive,aggregate-error,ansi-escapes

%check
%nodejs_symlink_deps --check
%if %{with test}
%{__nodejs} -e 'require("./")'
NODE_ENV=test %{_bindir}/%{srcmodule} -R tests
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files -n nodejs-%{srcmodule}
%doc node_modules/%{srcmodule}/CHANGELOG.md
%doc node_modules/%{srcmodule}/README.md
%license node_modules/%{srcmodule}/LICENSE.txt
%{nodejs_sitelib}/%{srcmodule}/
%{_bindir}/%{srcmodule}

%files -n nodejs-abort-controller
%doc node_modules/abort-controller/README.md
%license node_modules/abort-controller/LICENSE
%{nodejs_sitelib}/abort-controller/

%files -n nodejs-acorn
%doc node_modules/acorn/CHANGELOG.md
%doc node_modules/acorn/README.md
%license node_modules/acorn/LICENSE
%{nodejs_sitelib}/acorn/
%{_bindir}/acorn

%files -n nodejs-acorn-import-attributes
%doc node_modules/acorn-import-attributes/README.md
%license node_modules/acorn-import-attributes/LICENSE
%{nodejs_sitelib}/acorn-import-attributes/

%files -n nodejs-after-all-results
%doc node_modules/after-all-results/README.md
%license node_modules/after-all-results/LICENSE
%{nodejs_sitelib}/after-all-results/

%files -n nodejs-agentkeepalive
%doc node_modules/agentkeepalive/README.md
%license node_modules/agentkeepalive/LICENSE
%{nodejs_sitelib}/agentkeepalive/

%files -n nodejs-aggregate-error
%doc node_modules/aggregate-error/readme.md
%license node_modules/aggregate-error/license
%{nodejs_sitelib}/aggregate-error/

%files -n nodejs-ansi-escapes
%doc node_modules/ansi-escapes/readme.md
%license node_modules/ansi-escapes/license
%{nodejs_sitelib}/ansi-escapes/

%files -n nodejs-ansi-regex
%doc node_modules/ansi-regex/readme.md
%license node_modules/ansi-regex/license
%{nodejs_sitelib}/ansi-regex/

%files -n nodejs-ansi-styles
%doc node_modules/ansi-styles/readme.md
%license node_modules/ansi-styles/license
%{nodejs_sitelib}/ansi-styles/

%files -n nodejs-array-union
%doc node_modules/array-union/readme.md
%license node_modules/array-union/license
%{nodejs_sitelib}/array-union/

%files -n js-async
%doc node_modules/async/CHANGELOG.md
%doc node_modules/async/README.md
%license node_modules/async/LICENSE
%{_jsdir}/async/

%files -n nodejs-async
%doc node_modules/async/CHANGELOG.md
%doc node_modules/async/README.md
%license node_modules/async/LICENSE
%{nodejs_sitelib}/async/


