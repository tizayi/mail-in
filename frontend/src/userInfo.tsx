import "./App.css"
import {  Card, CardBody, Stack, Input, Select, Center, Button } from '@chakra-ui/react'

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
                <option value='person1'>person 1</option>
                <option value='person2'>person 2</option>
                <option value='person3'>person 3</option>
            </Select>
            <Button>Submit</Button>
        </Stack>
        </CardBody>
    </Card>
    </>)
}