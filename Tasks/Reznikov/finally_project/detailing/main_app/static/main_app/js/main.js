import {popupForm} from "./ajax/popup-form.js"
import { calendar } from "./calendar.js"
import { mobile_menu } from "./mobile_menu.js"
import {popup_days} from "./ajax/popup-days.js"
import {popup} from "./popup.js"

$(document).ready(() => {
    popupForm()
    calendar()
    mobile_menu()
    popup_days()
    popup()
})