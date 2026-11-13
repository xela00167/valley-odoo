/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class ValleyPage extends Component {
    static template = "valley_network.ValleyPage";

    joinValley() {
        window.open(
            "https://valleynetwork.eu/en/onboarding?utm_source=odoo_apps",
            "_blank"
        );
    }
}

registry.category("actions").add("valley_network.ValleyPage", ValleyPage);
