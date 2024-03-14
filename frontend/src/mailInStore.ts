import {create} from "zustand"
import {Holder, HolderInfo, Visit} from "./types"

type MailInStore = {
    visit: Visit,
    holder_info: HolderInfo,
    holder: Holder,
}

const useStore = create<MailInStore>((set) => ({
    visit: {
        id: "jvs",
        name:  "jvdjk",
        email: "hplc",
        phone_number: "th",
        local_contact: "hv",
    },
    holder_info: {
      id: "jvs",
      visit_id:  "jvdjk",
        type: "hplc",
        storage_temp: "room"
    },
    holder: {
        position_1 : undefined,
        position_2 : undefined,
        position_3 : undefined,
        position_4 : undefined,
        position_5 : undefined,
        position_6 : undefined,
        position_7 : undefined,
        position_8 : undefined,
        position_9 : undefined,
    },
}))

export default useStore