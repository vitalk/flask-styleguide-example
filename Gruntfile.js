module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),

    // Path to static assets
    assets: 'app/static',

    clean: {
      stylesheets: ['<%= assets %>/dist']
    },

    connect: {
      options: {
        hostname: 'localhost',
        port: 5008,
      },

      serve: {
        options: {
          // Prevents Grunt to close just after the task (starting the server)
          // completes
          keepalive: true,
          livereload: '<%= watch.options.livereload %>',
        }
      }
    },

    watch: {
      options: {
        livereload: 1348
      },

      stylesheets: {
        files: '<%= assets %>/stylesheets/**/*.less',
        // Remove compiled stylesheets to force assets rebuild
        tasks: 'clean:stylesheets'
      },

      javascript: {
        files: ['<%= assets %>/scripts/**/*.js']
      }
    }

  });

  // Cleanup source directory
  grunt.loadNpmTasks('grunt-contrib-clean');

  // The Big Brother watching you
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Development server with live reload
  grunt.loadNpmTasks('grunt-contrib-connect');

};
