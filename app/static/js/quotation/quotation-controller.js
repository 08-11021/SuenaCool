//controlador de cotizaciones
stohtModule.controller('quotationsController',
    ['$scope', '$location', '$route', 'flash', 'loginService', 'servicesService',
        function ($scope, $location, $route, flash, loginService, servicesService) {
            $scope.view= "quotations";

            // Level 23 means all can do
            loginService.check({'securityLvl': 23}).then(function (object) {
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

            // Custom content
            $scope.saveButton = "Crear Cotización";

            $scope.services = servicesService.services();
            
            //cierre de sesion
            $scope.logout = function() {
                loginService.logout().then(function(object){
                    $location.path('/');
                });

            };
        }]);
