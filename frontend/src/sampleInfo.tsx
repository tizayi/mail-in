import { useState } from "react";
import "./App.css"
import { Stack, Input, Select, Center, Textarea, Switch, HStack, Text } from '@chakra-ui/react'

export function HplcSampleInfo() {

    return (
      <>
          <Stack>
              <Center>Hplc Sample Info</Center>
                <Input placeholder='Name' />
                <Input placeholder="concentration"/>
                <Input placeholder="volume"/>
                <Input placeholder="Molecular weight"/>
                <Select placeholder='column'>
                  <option value='1'>column 1</option>
                  <option value='2'>4 column 2</option>
              </Select>
              <Textarea placeholder='notes' />
          </Stack>
      </>)
  }

  export function BatchSampleInfo() {
    const [isBuffer, setIsBuffer] = useState<boolean>(false)
    return (
      <>
        <Stack>
        <HStack>
            <Text>Buffer </Text>
            <Switch isChecked={isBuffer} onChange={(e) => setIsBuffer(e.target.checked)}/>
            <Text>Sample </Text>
          </HStack>
        { isBuffer ?
            <>
            <Center>Batch Sample Info</Center>
              <Input placeholder='Name' />
              <Input placeholder="concentration"/>
              <Input placeholder="volume"/>
              <Input placeholder="Molecular weight"/>
              <Input placeholder="Buffer position"/>
              <Textarea placeholder='notes' />
              </>
          :
          <>
          <Center>Buffer Info</Center>
          <BufferInfo/>
          </>

      }

          </Stack>
      </>)
  }

export function BufferInfo(){
  return (
    <>
    <Input placeholder='Buffer ID' />
    <Input placeholder="Buffer pH"/>
    </>
  )
}