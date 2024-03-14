export type HolderMode = "hplc" | "batch"

export interface Visit {
    id: string,
    name: string,
    email: string,
    phone_number: string,
    local_contact: string
}

export interface Buffer {
    id: string,
    name: string,
    holder_id: string,
    ph?: string,
    position?: number,
}

export interface Sample {
    id: string,
    name: string,
    holder_id: string,
    position: number,
    concentration?: number,
    volume?: number,
    molecular_weight?: number,
    column?: string,
    buffer_id: string
    notes?: string
}

export interface HolderInfo {
    id: string
    visit_id: string
    type: HolderMode
    storage_temp: string
}

export interface Holder {
    position_1?: HolderSlot, 
    position_2?: HolderSlot, 
    position_3?: HolderSlot, 
    position_4?: HolderSlot, 
    position_5?: HolderSlot,
    position_6?: HolderSlot, 
    position_7?: HolderSlot, 
    position_8?: HolderSlot, 
    position_9?: HolderSlot, 
}

export interface HolderSlot{
    type: "buffer" | "sample"
    sample: Sample,
    buffer: Buffer,
}

export interface MailInInput{
    user: Visit,
    holder: HolderInfo,
    samples: Sample[]
    buffers: Buffer[]
}


export function holder2Array(holder: Holder): {samples: Sample[], buffers: Buffer[]} {
    const samples: Sample[] = [];
    const buffers: Buffer[] = [];
    for (const [position,slot] of Object.entries(holder)){
        const position_num = parseInt(position.split("_")[1]);
        if (slot.type == "buffer"){
            slot.buffer.position = position_num;
            buffers.push(slot.buffer);
        } else {
            slot.sample.position = position_num;
            samples.push(slot.sample);
        }
    }
    return {samples: samples, buffers: buffers};
}