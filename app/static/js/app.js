// Creación del módulo de la aplicación
var stohtModule = angular.module('eventos', ['angularTreeview','ngRoute', 'ngAnimate', 'flash']);
stohtModule.config(function ($routeProvider) {
    $routeProvider.when('/', {
                controller: 'loginController',
                templateUrl: 'views/login/login.html'
            }).when('/signup', {
                controller: 'signupController',
                templateUrl: 'views/login/login.html'
            }).when('/userList', {
                controller: 'userListController',
                templateUrl: 'views/app/editUser.html'
            }).when('/editUser', {
                controller: 'editUserController',
                templateUrl: 'views/app/editUser.html'
            }).when('/home', {
                controller: 'userController',
                templateUrl: 'views/app/home.html'
            }).when('/profile', {
                controller: 'profileController',
                templateUrl: 'views/app/profile.html'
            }).when('/editProfile', {
                controller: 'editProfileController',
                templateUrl: 'views/app/profile.html'
            }).when('/categories', {
                controller: 'categoriesController',
                templateUrl: 'views/app/categories.html'
            }).when('/services', {
                controller: 'servicesController',
                templateUrl: 'views/app/services.html'
            }).when('/suscriptions', {
                controller: 'suscriptionsController',
                templateUrl: 'views/app/suscriptions.html'
            }).when('/requests', {
                controller: 'requestsController',
                templateUrl: 'views/app/requests.html'
            }).when('/quotations', {
                controller: 'quotationsController',
                templateUrl: 'views/app/quotations.html'
            })
});

stohtModule.controller('stohtController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "login";
}]);


/*
    angular.treeview.js
*/
(function(l){
	l.module("angularTreeview",[]).directive("treeModel",function($compile){
		return{
			restrict:"A",link:function(a,g,c){
				var e=c.treeModel,
				 h=c.nodeLabel || "label",
				 d=c.nodeChildren || "children",
				 k ='<ul><li data-ng-repeat="node in '+e+'" ng-init= "node.collapsed = true"><i class="collapsed" data-ng-show="node.'+d+'.length && node.collapsed" data-ng-click="selectNodeHead(node, $event)"></i><i class="expanded" data-ng-show="node.'+d+'.length && !node.collapsed" data-ng-click="selectNodeHead(node, $event)"></i><i class="normal" data-ng-hide="node.'+	d+'.length"></i><span data-ng-class="node.selected" data-ng-click="selectNodeLabel(node, $event)">{{node.'+h+'}}</span><div data-ng-hide="node.collapsed" data-tree-model="node.'+d+'" data-node-id='+(c.nodeId||"id")+" data-node-label="+h+" data-node-children="+d+"></div></li></ul>";
			e && e.length && (c.angularTreeview?(a.$watch(e,function(m,b){
					g.empty().html($compile(k)(a))
				},!1),a.selectNodeHead=a.selectNodeHead||function(a,b){
					b.stopPropagation&&b.stopPropagation();
					b.preventDefault&&b.preventDefault();
					b.cancelBubble=!0;
					b.returnValue=!1;
					a.collapsed=!a.collapsed
				},a.selectNodeLabel=a.selectNodeLabel||function(c,b){
					b.stopPropagation&&b.stopPropagation();
					b.preventDefault&&b.preventDefault();
					b.cancelBubble=!0;
					b.returnValue=!1;
					a.currentNode&&a.currentNode.selected&&(a.currentNode.selected=void 0);
					c.selected="selected";
					a.currentNode=c}
					):g.html($compile(k)(a)))}
				}
			}
			)}
)(angular);
