export type HolderMode = "hplc" | "batch"

export interface Visit {
    name: string,
    visit_id: string,
    email: string,
    phone_number: string,
    local_contact: string
}

export interface Buffer {
    id: string,
    ph?: string,
    position: number
}

export interface HplcSample {
    name: string,
    position: number,
    concentration?: number,
    volume?:number,
    molecular_weight?:number,
    column?: string,
    notes?: string
}

export interface BatchSample {
    name: string,
    position: number,
    concentration?: number,
    volume?:number,
    molecular_weight?:number,
    buffer_position: number,
    notes?: string
}

export interface BatchHolder {
    storage_temp: string,
    holder_id: string,
    samples: BatchSample[],
    buffers: Buffer[]
}

export interface HPLCHolder{
    storage_temp: string,
    holder_id: string,
    samples: HplcSample[],
    buffer: Buffer
}