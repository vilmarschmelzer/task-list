var requestapp = angular.module('task',[]);

requestapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

requestapp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

requestapp.controller('Task', function Task($scope, $log, $http){

    $scope.task = null;
    $scope.load_tasks = function(){

        $http.get('/task/')
        .success(function (data, status, headers, config) {
            $scope.tasks = data;
        })
        .error(function (data, status, header, config) {

        });
    };

    $scope.delete = function(task_id){

        $http.delete('/task/'+task_id+'/')
        .success(function (data, status, headers, config) {
            $scope.load_tasks();
        })
        .error(function (data, status, header, config) {

        });
    };

    $scope.done = function(task_id){

        var data = $.param({id: task_id});

        var config = {
            headers : {
                'Content-Type': 'application/json'
            }
        }

        $http.get('/done-task/'+task_id+'/')
        .success(function (data, status, headers, config) {
            $scope.load_tasks();
        })
        .error(function (data, status, header, config) {

        });
    };

    $scope.alter = function(task_id){

        $http.get('/get-task/'+task_id+'/')
        .success(function (data, status, headers, config) {
            $scope.task = data;

            $('#modal_task').modal('show');

        })
        .error(function (data, status, header, config) {
            $scope.load_tasks();
        });
    }

    $scope.new = function(){

        if($scope.task != null){

            $scope.task.id=null;
            $scope.task.task='';
            $scope.task.done=false;
        }

        $('#modal_task').modal('show');
    }
    $scope.save = function(){

        var data = $.param($scope.task);
        var config = {
            headers : {
                'Content-Type': 'application/json'
            }
        }

        $http.post('/task/', $scope.task, config)
        .success(function (data, status, headers, config) {
            $scope.task.null;
            $('#modal_task').modal('hide');

            $scope.load_tasks();

        })
        .error(function (data, status, header, config) {

        });
    }
});