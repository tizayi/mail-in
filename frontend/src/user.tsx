import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center } from '@chakra-ui/react'

export default function UserInfo() {

  return (
    <>
    <Card>
        <CardBody>
        <Stack>
            <Center>User Info</Center>
            <Input placeholder='Name' />
            <Input placeholder='Visit ID' />
            <Input placeholder='Email' />
            <Input placeholder='Phone Number' />
            <Select placeholder='Local Contact'>
                <option value='option1'>Option 1</option>
                <option value='option2'>Option 2</option>
                <option value='option3'>Option 3</option>
            </Select>
        </Stack>
        </CardBody>
    </Card>
    </>)
}