import "./App.css"
import {  Card, CardBody, Stack, Input, Center } from '@chakra-ui/react'

export default function BufferInfo() {

    return (
      <>
      <Card>
          <CardBody>
          <Stack>
              <Center>Buffer Info</Center>
              <Input placeholder='Buffer ID' />
              <Input placeholder="pH"/>
              <Input placeholder="position"/>
          </Stack>
          </CardBody>
      </Card>
      </>)
  }
