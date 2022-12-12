
a = {
    'oldValue': {

    },
    'updateMask': {

    },
    'value': {
        'createTime': '2022-12-04T14:39:31.490127Z',
        'fields': {
            'created_time': {
                'timestampValue': '2022-12-04T14:39:31.391Z'
            },
            'display_name': {
                'stringValue': 'rassoi app'
            },
            'email': {
                'stringValue': 'rassoi.app@gmail.com'
            },
            'photo_url': {
                'stringValue': 'https://lh3.googleusercontent.com/a/AEdFTp76P1NPKVb1Xe02PoYohT484P2sGJDulI2mQDLo=s96-c'
            },
            'uid': {
                'stringValue': '2Si5RuOy0DRSooL3C4Hiyhgjycj2'
            }
        },
        'name': 'projects/rassoi-767af/databases/(default)/documents/users/2Si5RuOy0DRSooL3C4Hiyhgjycj2',
        'updateTime': '2022-12-04T14:39:31.490127Z'
    }
}
print(a["value"]["fields"]["uid"]["stringValue"])
