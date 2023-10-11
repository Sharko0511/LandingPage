/** @odoo-module **/

import { _lt } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

import { Component } from "@odoo/owl";

export class ImgField extends Component {
}
ImgField.displayName = _lt("Text");
ImgField.supportedTypes = ["char"];
ImgField.template = "web.ImgField";
registry.category("fields").add("img", ImgField);