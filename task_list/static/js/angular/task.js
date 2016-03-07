var requestapp = angular.module('task',[]);
var dialog = document.querySelector('dialog');

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

    $scope.done = function(task){
        task.done=true;

        var config = {
            headers : {
                'Content-Type': 'application/json'
            }
        }

        $http.put('/task/'+task.id+'/', task)
        .success(function (data, status, headers, config) {
            $scope.load_tasks();
        })
        .error(function (data, status, header, config) {

        });
    };

    $scope.alter = function(task_id){

        $http.get('/task/'+task_id+'/')
        .success(function (data, status, headers, config) {
            $scope.task = data;

            dialog.showModal();

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

        dialog.showModal();
    }
    $scope.save = function(){
        var config = {
            headers : {
                'Content-Type': 'application/json'
            }
        }

        if($scope.task.id == null){

            $http.post('/task/', $scope.task, config)
            .success(function (data, status, headers, config) {
                $scope.task.null;
                dialog.close();

                $scope.load_tasks();

              })
              .error(function (data, status, header, config) {

            });
        }
        else{
            $http.put('/task/'+$scope.task.id+'/', $scope.task, config)
            .success(function (data, status, headers, config) {
                $scope.task.null;
                dialog.close();

                $scope.load_tasks();

              })
              .error(function (data, status, header, config) {

            });
        }
    }
});
