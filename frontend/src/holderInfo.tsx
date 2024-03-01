import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center } from '@chakra-ui/react'
import HolderDiagram from "./holderDiagram"
import {HolderMode} from "./types"
import { useState } from "react"

export default function HolderInfo() {
    const [mode, setMode] = useState<HolderMode>("hplc");
    return (
      <>
      <Stack>
      <Card>
          <CardBody>
          <Stack>
              <Center>Holder</Center>
              <Input placeholder='Holder ID' />
              <Select placeholder='Storage Temp'>
                  <option value='room'>room</option>
                  <option value='4  '>4 &deg;C</option>
                  <option value='-80'>-80 &deg;C</option>
              </Select>
              <Select placeholder='Mode' value={mode} onChange={(e) => setMode(e.target.value as HolderMode)}>
                  <option value='hplc'>HPLC</option>
                  <option value='batch'>Batch</option>
              </Select>
          </Stack>
          </CardBody>
      </Card>
      <HolderDiagram mode={mode}/>
      </Stack>
      </>)
  }
