/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks"

class HospitallListController extends ListController {
    setup() {
        super.setup()
        console.log("This is res partner controller")
        this.action = useService("action")
    }

    openNewView() {
        console.log("Open New view")
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Daily Revenue",
            res_model: "daily.revenue",
            views: [[false, "list"], [false, "form"]]
        })
    }
}

export const hospitalListView = {
    ...listView,
    Controller: HospitallListController,
    buttonTemplate: "tree_app.stops",

}

registry.category("views").add("hospital_list_view", hospitalListView)