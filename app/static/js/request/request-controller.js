//controlador de peticiones
stohtModule.controller('requestsController',
   ['$scope', '$location', '$route', 'flash', 'requestsService','categoryService','loginService',
    function ($scope, $location, $route, flash, requestsService, categoryService, loginService) {
        $scope.view= "requests";

        loginService.check({'securityLvl': 2}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];

                    $scope.isAdmin= ($scope.actorRol & 1) !== 0;
                    $scope.isOperator= ($scope.actorRol & 2) !== 0;
                    $scope.isClient = ($scope.actorRol & 4) !==0;
                    $scope.isManager = ($scope.actorRol & 16) !==0;
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";
        requestsService.requests({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.requests = object.data['result'];
            }else{
                $scope.requests = [];
            }
          });

        $location.search({});

        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };
    }]);
