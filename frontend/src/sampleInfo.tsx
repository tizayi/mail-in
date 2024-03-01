import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center, Textarea } from '@chakra-ui/react'

export function HplcSampleInfo() {

    return (
      <>
      <Card>
          <CardBody>
          <Stack>
              <Center>Hplc Sample Info</Center>
                <Input placeholder='Name' />
                <Input placeholder='position'/>
                <Input placeholder="concentration"/>
                <Input placeholder="volume"/>
                <Input placeholder="Molecular weight"/>
                <Select placeholder='column'>
                  <option value='1'>column 1</option>
                  <option value='2'>4 column 2</option>
              </Select>
              <Textarea placeholder='notes' />
          </Stack>
          </CardBody>
      </Card>
      </>)
  }
  export function BatchSampleInfo() {

    return (
      <>
      <Card>
          <CardBody>
          <Stack>
              <Center>Batch Sample Info</Center>
                <Input placeholder='Name' />
                <Input placeholder='position'/>
                <Input placeholder="concentration"/>
                <Input placeholder="volume"/>
                <Input placeholder="Molecular weight"/>
                <Input placeholder="Buffer position"/>
                <Textarea placeholder='notes' />
          </Stack>
          </CardBody>
      </Card>
      </>)
  }
