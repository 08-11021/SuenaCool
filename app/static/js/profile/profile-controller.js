//Controlador del perfil de usuario
stohtModule.controller('profileController',
   ['$scope', '$location', '$route', 'flash', 'loginService', 'profileService',
    function ($scope, $location, $route, flash, loginService, profileService) {
        $scope.view = "profile";
      loginService.check({'securityLvl': 2}).then(function (object) {
            if (object.data['redirect'] == undefined) {
                $scope.actorName = object.data['actorName'];
                $scope.actorRol = object.data['actorRol'];
                $scope.actorEmail = object.data['actorEmail'];

                $scope.isAdmin= ($scope.actorRol & 1) !== 0;
                $scope.isOperator= ($scope.actorRol & 2) !== 0;
                $scope.isClient = ($scope.actorRol & 4) !==0;
                $scope.isManager = ($scope.actorRol & 16) !==0;

                profileService.getProfile({email: $scope.actorEmail})
                  .then(function(response) {
                    $scope.profile = response.data;
                  });
            } else {
                $location.path(object.data['redirect']);
            }
        });

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

      }]);

//Controlador del perfil de usuario
stohtModule.controller('editProfileController',
   ['$scope', '$location', '$route', 'flash', 'loginService', 'profileService',
    function ($scope, $location, $route, flash, loginService, profileService) {
        $scope.view = "editProfile";
      loginService.check({'securityLvl': 2}).then(function (object) {
            if (object.data['redirect'] == undefined) {
                $scope.actorName = object.data['actorName'];
                $scope.actorRol = object.data['actorRol'];
                $scope.actorEmail = object.data['actorEmail'];

                $scope.isAdmin= ($scope.actorRol & 1) !== 0;
                $scope.isOperator= ($scope.actorRol & 2) !== 0;
                $scope.isClient = ($scope.actorRol & 4) !==0;
                $scope.isManager = ($scope.actorRol & 16) !==0;

                profileService.getProfile({email: $scope.actorEmail})
                  .then(function(response) {
                    $scope.profile = response.data;
                  });
            } else {
                $location.path(object.data['redirect']);
            }
        });

        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

        $scope.sendForm = function() {
            profileService.editProfile($scope.profile)
              .then(function(response){
                $location.path('/profile')
              });
        }

        }]);

