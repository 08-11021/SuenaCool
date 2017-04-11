//controlador de registro
stohtModule.controller('signupController',
   ['$scope', '$location', '$route', 'flash', 'signupService','loginService',
    function ($scope, $location, $route, flash, signupService, loginService) {
        loginService.check({'securityLvl': 0}).then(function (object) {
            $scope.view="signup";
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";

        //Registrar
        $scope.save = function() {
            if ($scope.password == $scope.passwordr) {
                signupService.signup({
                    email: $scope.email,
                    password: $scope.password,
                    rol: 6,
                    fullName: $scope.fullName
                }).then(function (object) {
                    if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $location.path('/');
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
                });
            }else{
                $scope.msg="Las contraseñas no coinciden";
            }

      };

        //volver al login
        $scope.login = function() {
            $location.path('/');
        };

    }]);


