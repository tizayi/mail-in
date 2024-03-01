import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center } from '@chakra-ui/react'

export default function HolderInfo() {

    return (
      <>
      <Card>
          <CardBody>
          <Stack>
              <Center>Holder Info</Center>
              <Input placeholder='Holder ID' />
              <Select placeholder='Storage Temp'>
                  <option value='room'>room</option>
                  <option value='4  '>4 &deg;C</option>
                  <option value='-80'>-80 &deg;C</option>
              </Select>
              <Select placeholder='Mode'>
                  <option value='room'>HPLC</option>
                  <option value='4  '>Batch</option>
              </Select>
          </Stack>
          </CardBody>
      </Card>
      </>)
  }
