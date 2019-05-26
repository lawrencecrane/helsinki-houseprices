var gulp = require('gulp');
var run = require('gulp-run');

gulp.task('build-vuokraovi', function () {
  gulp.watch('./src/*.js', function () {
    return run('npm run build').exec();
  });
});
