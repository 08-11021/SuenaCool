//Controlador del home (usuario)
stohtModule.controller('userController',
   ['$scope', '$location', '$route', 'flash', 'userService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        $scope.view = "home";
        loginService.check({'securityLvl': 63}).then(function (object) {
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

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

    }]);
