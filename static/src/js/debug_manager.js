odoo.define('remote_debug.DebugManager', function (require) {
    "use strict";
    
    var DebugManager = require('web.DebugManager');
    
    DebugManager.include({
        remote_debug: function () {
            var self = this,
                context = {};
            
            var action = {
                    type: 'ir.actions.act_window',
                    res_model: 'remote.debug.settings',
                    view_mode: 'form',
                    view_type: 'form',
                    views: [[false, 'form']],
                    target: 'inline',
                    context: context,
            };
            
            self.do_action(action);
        }
    });
    
});
    