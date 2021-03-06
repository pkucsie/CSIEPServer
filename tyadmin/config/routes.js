[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: '认证和授权',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: '权限',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: '组',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            }
        ]
    },
    {
        name: '双创平台',
        icon: 'BarsOutlined',
        path: '/xadmin/app_api',
        routes:
        [
            {
                name: '时间线',
                path: '/xadmin/app_api/task_timeline',
                component: './AutoGenPage/TaskTimelineList',
            },
            {
                name: '机构',
                path: '/xadmin/app_api/organization',
                component: './AutoGenPage/OrganizationList',
            },
            {
                name: '嘉宾',
                path: '/xadmin/app_api/vip_guest',
                component: './AutoGenPage/VipGuestList',
            },
            {
                name: '评委',
                path: '/xadmin/app_api/judge',
                component: './AutoGenPage/JudgeList',
            },
            {
                name: '首页Banner',
                path: '/xadmin/app_api/slider',
                component: './AutoGenPage/SliderList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
