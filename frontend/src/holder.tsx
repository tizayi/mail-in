import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center } from '@chakra-ui/react'

export function HolderInfo() {

    return (
      <>
      <Card>
          <CardBody>
          <Stack>
              <Center>Batch Holder Info</Center>
              <Input placeholder='Holder ID' />
              <Select placeholder='Storage Temperature'>
                  <option value='room'>room</option>
                  <option value='4  '>4 &deg;C</option>
                  <option value='-80'>-80 &deg;C</option>
              </Select>
          </Stack>
          </CardBody>
      </Card>
      </>)
  }
