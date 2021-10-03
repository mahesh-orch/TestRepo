/* global angular */
angular.module('main')
  .constant('st2Config', {

    // In case you want to override default value for the result sizes we still render in the
    // history details widget. Keep in mind that anything above 200-500 KB will take a long time to
    // render and likely freeze the browser window for deeply nested JSON object results.
    // Value is in bytes.
    // max_execution_result_size_for_render: 200 * 1024,
    //
    // Set to true to display StackStorm and st2web version in the header
    //show_version_in_header: false;

    // hosts: [
    //   {
    //     name: 'Dev Env',
    //     url: 'https://:443/api',
    //     auth: 'https://:443/auth',
    //     stream: 'https://:443/stream',
    //   },
    //   {
    //     name: 'Express',
    //     url: '//172.168.90.50:9101/api',
    //     auth: '//172.168.90.50:9101/auth',
    //   },
    // ],

  });
