//Controlador del home (administrador)
stohtModule.controller('adminController',
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        loginService.check({'securityLvl': 1}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];
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

//controlador de edicion de usuario (administrador)
stohtModule.controller('editUserController',
   ['$scope', '$location', '$route', 'flash', 'adminService','loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        $scope.view = "editUser";
        $scope.admin=0;
        $scope.operator=0;
        $scope.client=0;
        $scope.director=0;
        $scope.manager=0;
        $scope.budget=0;
        loginService.check({'securityLvl': 1}).then(function (object) {
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
        $scope.changeMail = "checked";
        $scope.formTitle = "Editar Usuario";
        $scope.saveButton = "Actualizar";

        $scope.id=$location.search()['user'];

        //Obtener datos de usuario
        adminService.getUser({id: $scope.id}).then(function (object) {
            if(object.data['error'] != undefined){
              $scope.error = object.data['error'];
            }else{

                $scope.id=object.data['id'];
                $scope.email=object.data['email'];
                $scope.password="";
                $scope.passwordr="";
                $scope.fullName=object.data['fullName'];
                $scope.admin=object.data['admin'];
                $scope.operator=object.data['operator'];
                $scope.client=object.data['client'];
                $scope.director=object.data['director'];
                $scope.manager=object.data['manager'];
                $scope.budget=object.data['budget'];
            }
          });


        //Guardar cambios
        $scope.save = function() {
            if ($scope.password == $scope.passwordr) {
                adminService.updateUser({
                    email: $scope.email,
                    password: $scope.password,
                    rol: $scope.admin + $scope.operator + $scope.client + $scope.director + $scope.manager + $scope.budget,
                    fullName: $scope.fullName
                }).then(function (object) {
                    if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        $location.path('/userList');
                    }
                });
            }else{
                $scope.msg="Las contraseñas no coinciden";
            }

      };


        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };

    }]);

//controlador de creacion de usuarios y lista de usuarios (administrador)
stohtModule.controller('userListController',
   ['$scope', '$location', '$route', 'flash', 'adminService','loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
        $scope.view= "userList";
        $scope.admin=0;
        $scope.operator=2;
        $scope.client=4;
        $scope.director=0;
        $scope.manager=0;
        $scope.budget=0;

        loginService.check({'securityLvl': 1}).then(function (object) {
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
        $scope.changeMail = "";
        $scope.formTitle = "Nuevo Usuario";
        $scope.saveButton = "Crear";

        $location.search({});

        //Ver usuario
        $scope.viewUser = function(id) {
            $location.search('user', id);
            $location.path('/editUser');
        };

        //Obtener Lista de usuarios
        adminService.users({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.users = object.data['result'];
            }else{
                $scope.users = [];
            }
          });

        //Crear usuario
        $scope.save = function() {
            if ($scope.password == $scope.passwordr){
                $scope.rol = $scope.admin + $scope.operator + $scope.client + $scope.director + $scope.manager + $scope.budget;
                adminService.createUser({email: $scope.email, password: $scope.password, rol:$scope.rol, fullName: $scope.fullName}).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {

                            $scope.email="";
                            $scope.password="";
                            $scope.passwordr="";
                            $scope.fullName="";
                            $scope.msg = "";
                            $scope.msg = object.data['reason'];
                            adminService.users({}).then(function (object) {
                                if(object.data['result'] != undefined){
                                    $scope.users = object.data['result'];
                                }else{
                                    $scope.users = [];
                                }
                            });
                            $location.path('/userList');
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
              });
            }else{
                $scope.msg="Las contraseñas no coinciden";
            }

      };

        //Eliminar usuario
        $scope.delete = function(id) {
                adminService.deleteUser({userId: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.email="";
                    $scope.password="";
                    $scope.passwordr="";
                    $scope.fullName="";
                    $scope.msg = "";
                    $scope.msg = object.data['reason'];

                    //Recargar lista de usuarios
                    adminService.users({}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.users = object.data['result'];
                        }else{
                            $scope.users = [];
                        }
                  });

                  $location.path('/userList');
                }
              });

      };

        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };
    }]);
