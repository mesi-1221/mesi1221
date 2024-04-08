odoo.define('Addis_system_withholding.handle_checkbox_widget', function (require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');

    var HandleCheckboxWidget = AbstractField.extend({
        supportedFieldTypes: ['boolean'],

        init: function () {
            this._super.apply(this, arguments);
            this.set("clickable", true);
        },

        _render: function () {
            this.$el.addClass('clickable');
            this.$el.text(this.value);
        },

        _onClick: function () {
            this.trigger_up('field_changed', {
                dataPointID: this.dataPointID,
                changes: { withholding_checkbox: !this.value },
            });
        },
    });

    fieldRegistry.add('handle_checkbox', HandleCheckboxWidget);

    return HandleCheckboxWidget;
});